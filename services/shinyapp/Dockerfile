FROM sktrinh12/meta-shinybase:latest

ARG UNAME
ARG PASSWORD
ENV UNAME $UNAME
ENV APP_HOME "/home/${UNAME}"
ENV PASSWORD $PASSWORD

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

RUN useradd -m -d $APP_HOME "${UNAME}" \
    && chown -R ${UNAME}:${UNAME} $APP_HOME \
    && echo "${UNAME}:${PASSWORD}" | chpasswd

COPY app $APP_HOME/app

RUN R -e 'install.packages("shinyFiles")'
RUN chown -R $UNAME:$UNAME $APP_HOME

EXPOSE 3838
CMD ["R", "-e", "shiny::runApp('/home/bdb/app', host= '0.0.0.0', port = 3838)"]
