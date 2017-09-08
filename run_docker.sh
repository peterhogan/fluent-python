sudo docker run --rm \
		-it  \
		--name pydock\
		--hostname pydock\
		-p 80:5000\
		-v /home/pine/fluent-python:/usr/src/app \
		textract:latest \
		bash
