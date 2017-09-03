sudo docker run --rm \
		-it  \
		--name pydock\
		--hostname pydock\
		-v /home/pine/fluent-python:/usr/src/app \
		alpha:latest \
		bash
