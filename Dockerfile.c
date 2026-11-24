FROM golang:1.20-alpine AS build

WORKDIR /src
COPY service-c/go.mod ./go.mod
COPY service-c/main.go ./main.go
RUN go build -o /service-c .

FROM alpine:3.18

COPY --from=build /service-c /service-c
EXPOSE 8080
CMD ["/service-c"]
