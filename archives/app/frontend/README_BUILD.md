```Bash
docker image build -t app-backend:$(git rev-parse --abbrev-ref HEAD | sed 's/[^a-zA-Z0-9]/-/g') ./
```
