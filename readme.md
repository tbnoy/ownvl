# Deployment

make sure you have: 
- npm
- node

Now if you want to deploy the app, you will need to set AWS token and secret with:

`./node_modules/.bin/serverless config credentials --provider aws --key yyyyy --secret xxxxx`

After the above you can run the deploy command for dev:
`npm run deploy-dev`

After the above you can run the deploy command for production:
`npm run deploy-prod`

For viewing logs:
`npm run logs`

# Development

so instead of polutting each of our own envs with python3, node, packages etc.

We now have a small docker container that will hold it for use.

first build, run:
- `docker-compose build`
- `docker-compose up -d`

Now you have the container up and running.

You can "ssh" to the container with:

`docker-compose exec python /bin/bash`

For running the scripts, you can use:

- `make run`
  - this will run `python handler.py` with no serverless mocks
- `make svl`
  - this will run serverless the "right way"