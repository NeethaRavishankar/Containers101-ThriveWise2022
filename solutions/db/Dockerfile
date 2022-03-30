FROM amazon/dynamodb-local
WORKDIR /home/dynamodblocal
RUN mkdir ./db && chown -R 1000 ./db
EXPOSE 8080
CMD ["-jar", "DynamoDBLocal.jar", "-dbPath", "./db", "-sharedDb", "-port", "8080"]
VOLUME ["./db"]
