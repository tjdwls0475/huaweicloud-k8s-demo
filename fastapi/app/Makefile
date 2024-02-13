# Build Docker image
build:
    docker build -t fastapi:0.4 .

# Run Docker container
run:
    docker run -d -p 8000:80 --name harry-fastapi2 fastapi:0.4

# Tag Docker image for Huawei Cloud Repo
tag:
    docker tag fastapi:0.4 swr.ap-southeast-3.myhuaweicloud.com/harry-swr/fastapi:0.4

# Push Docker image to Huawei Cloud Repo
push:
    docker push swr.ap-southeast-3.myhuaweicloud.com/harry-swr/fastapi:0.4
