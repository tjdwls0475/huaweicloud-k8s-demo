# huaweicloud-k8s-demo
- Python의 FastAPI 프레임워크를 통해 Huawei Cloud의 Serverless K8s를 검증합니다.
순서는 아래와 같습니다.

## 1. FastAPI APP을 검증합니다.
   - 여기서는 간단하게 '/'로 request를 받아서 response를 내보낼 수 있는지 단순하게 routing을 정의하였습니다.
   - 모든 대역 0.0.0.0에서 트래픽이 유입될 수 있도록 하였으며, 서비스 포트는 80입니다.
  
## 2. 앱에 필요한 Library들을 requirements.txt에 적습니다.
   - 현재는 uvicorn과 fastapi만으로 충분합니다.

## 3. Docker Image를 정의합니다.
   - /src 디렉터리를 생성하여 앱 소스를 복사한 다음, 앱에 필요한 Library를 pip 커맨드로 설치합니다.
   - 80 포트로 컨테이너가 트래픽을 받을 수 있도록 합니다.
   - 앱의 시작점은 main.py로 합니다.

## 4. Docker Image를 빌드합니다.

## 5. 빌드된 Image로 컨테이너를 생성하여 앱의 정상 동작 유무를 검증합니다.

## 6. Docker Image를 태깅합니다.

## 7. 태깅된 Docker Image를 Huawei Cloud로 푸시합니다.

## 8. Deployment와 ConfigMap YAML 파일을 작성합니다.

## 9. 작성된 YAML 파일을 Huawei Cloud의 CCI(Cloud Container Instance)에서 배포해줍니다.

## 10. 배포된 Deployment를 LoadBalancer 타입의 Service로 노출해서 앱에 잘 접속되는지 확인합니다.
