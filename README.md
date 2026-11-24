# Aikido Monorepo Security Test

This repository contains three independent sample services:

- `service-a/`: Node.js/Express service
- `service-b/`: Python/Flask service
- `service-c/`: Go/Gin service

The root Dockerfiles build each service separately:

- `Dockerfile.a`
- `Dockerfile.b`
- `Dockerfile.c`

The sample code and dependency versions intentionally include detectable SAST and SCA issues for responsibility and repository-path limitation testing.
