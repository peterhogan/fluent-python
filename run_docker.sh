sudo docker run --rm \
		-it  \
		--name python-docker\
		--hostname pydock\
		-v /home/pine/fluent-python:/usr/src/app \
		alpha:latest \
		bash
