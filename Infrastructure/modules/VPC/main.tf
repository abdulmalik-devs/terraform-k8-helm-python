# Creating VPC, Name, CIDR amd Tags
resource "aws_vpc" "dev_vpc" {
  cidr_block                = "10.0.0.0/16"
  instance_tenancy          = "default"
  enable_dns_hostnames      = "true"
  enable_dns_support        = "true"

  tags = {
    Name = var.vpc_name
  }
}

# Creating availability zone using data source
data "aws_availability_zones" "available_az" {}

# Creating Public Subnet 1A in VPC
resource "aws_subnet" "public_subnet_1a" {
  vpc_id                    = aws_vpc.dev_vpc.id
  cidr_block                = "10.0.1.0/24"
  map_public_ip_on_launch   = "true"
  availability_zone         = data.aws_availability_zones.available_az.names[0]

  tags = {
    "Name" = "public_subnet_1a"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/clutser/dev_cluster" = "owned"
  }
}

# Creating Public Subnet 1B in VPC
resource "aws_subnet" "public_subnet_1b" {
  vpc_id                    = aws_vpc.dev_vpc.id
  cidr_block                = "10.0.2.0/24"
  map_public_ip_on_launch   = "true"
  availability_zone         = data.aws_availability_zones.available_az.names[1]

  tags = {
    "Name" = "public_subnet_1b"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/clutser/dev_cluster" = "owned"
  }
}

# Creating Private Subnet 1A in VPC
resource "aws_subnet" "private_subnet_1a" {
  vpc_id                    = aws_vpc.dev_vpc.id
  cidr_block                = "10.0.3.0/24"
  map_public_ip_on_launch   = "false"
  availability_zone         = data.aws_availability_zones.available_az.names[2]

  tags = {
    "Name" = "private_subnet_1a"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/clutser/dev_cluster" = "owned"
  }
}

# Creating Private Subnet 1B in VPC
resource "aws_subnet" "private_subnet_1b" {
  vpc_id                    = aws_vpc.dev_vpc.id
  cidr_block                = "10.0.4.0/24"
  map_public_ip_on_launch   = "false"
  availability_zone         = data.aws_availability_zones.available_az.names[3]

  tags = {
    "Name" = "private_subnet_1b"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/clutser/dev_cluster" = "owned"
    
  }
}

# Creating Internet Gateway in AWS VPC
resource "aws_internet_gateway" "igw" {
  vpc_id  = aws_vpc.dev_vpc.id

  tags = {
    Name  = "dev_igw"
  }
}

# Creating Route Tables for Internet gateway
resource "aws_route_table" "route-igw" {
  vpc_id            = aws_vpc.dev_vpc.id
  route {
    cidr_block      = "0.0.0.0/0"
    gateway_id      = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "Route-IGW"
  }
}

# Creating Nat Gateway for Private Subnet 1a
resource "aws_eip" "nat_1a" {
  vpc = true

  tags = {
    Name = "nat1"
  }
}

# Attaching Nat Gateway to Public Subnet 1a
resource "aws_nat_gateway" "nat_igw_1a" {
  allocation_id = aws_eip.nat_1a.id
  subnet_id     = aws_subnet.public_subnet_1a.id
  depends_on    = [aws_internet_gateway.igw]

  tags = {
    Name = "nat1"
  }
}

# Creating Nat Gateway for Private Subnet 1b
resource "aws_eip" "nat_1b" {
  vpc = true

  tags = {
    Name = "nat2"
  }
}

# Attaching Nat Gateway to Public Subnet 1b
resource "aws_nat_gateway" "nat_igw_1b" {
  allocation_id = aws_eip.nat_1b.id
  subnet_id     = aws_subnet.public_subnet_1b.id
  depends_on    = [aws_internet_gateway.igw]

  tags = {
    Name = "nat2"
  }
}

# Adding routes for private subnet 1a to Internet Gateway
resource "aws_route_table" "route-nat-1a" {
  vpc_id = aws_vpc.dev_vpc.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_igw_1a.id
  }
  tags = {
    Name = "route-nat-1a"
  }
}

# Adding routes for private subnet 1b to Internet Gateway
resource "aws_route_table" "route-nat-1b" {
  vpc_id = aws_vpc.dev_vpc.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_igw_1b.id
  }
  tags = {
    Name = "route-nat-1b"
  }
}

# Creating route associations for private subnets 1a
resource "aws_route_table_association" "route_private_1a" {
  subnet_id      = aws_subnet.private_subnet_1a.id
  route_table_id = aws_route_table.route-nat-1a.id
}

# Creating route associations for private subnets 1b
resource "aws_route_table_association" "route_private_1b" {
  subnet_id      = aws_subnet.private_subnet_1b.id
  route_table_id = aws_route_table.route-nat-1b.id
}

# Creating Route Associations public subnets 1a
resource "aws_route_table_association" "route_public_1a" {
  subnet_id          = aws_subnet.public_subnet_1a.id
  route_table_id     = aws_route_table.route-igw.id
}

# Creating Route Associations public subnets 1b
resource "aws_route_table_association" "route_public_1b" {
  subnet_id          = aws_subnet.public_subnet_1b.id
  route_table_id     = aws_route_table.route-igw.id
}
