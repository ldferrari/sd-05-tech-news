FROM python
RUN useradd -ms /bin/bash lizzard
RUN chown -R lizzard /home/lizzard/
WORKDIR /home/lizzard/
COPY . .
RUN apt-get update && apt-get install -y python3-venv && \
    python3 -m venv .venv && \
    python3 -m pip install -r dev-requirements.txt
USER lizzard
# docker run -it -v $PWD/tech_news:/home/lizzard/tech_news lizzardmedeiros/technews bash
