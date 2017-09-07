sudo docker run --rm \
		-it  \
		--name pydock\
		--hostname pydock\
		-p 8080:5000\
		-v /home/pine/fluent-python:/usr/src/app \
		gamma:latest \
		bash
