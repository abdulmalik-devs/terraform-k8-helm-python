provider "aws" {
  region = "us-west-2"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  /* backend "s3" {
    bucket = "terra-k8"
    key    = "tf-statefile/terraform.tfstate"
    region = "us-west-2"
  } */
}
