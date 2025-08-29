

resource "aws_ebs_volume" "example" {
  availability_zone = "us-west-2a"
  size              = 100
  type = gp3

  tags = {
    Name = "HelloWorld"
  }
}



===========
terraform: complete
 - terraform interview qsn's

AWS 
 - Interview qsn's

Plus Kuberenetes 
 - k8s interview qsn's
-----------
devops interview qns + lINUX 