#!/bin/bash

export $(xargs </home/.env)

prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="postgresql+asyncpg://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/prefect"

/usr/local/bin/python deployment.py 
echo "Deploy Pykrx deployment"
prefect agent start  --work-queue "wq_stock_etl" &
echo "Agent start"
prefect orion start --host 0.0.0.0