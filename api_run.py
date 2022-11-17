from app import create_api_app
import py_eureka_client.eureka_client as eureka_client
import socket
app = create_api_app()

#localIP = socket.gethostbyname(socket.gethostname())

#eureka_client.init(eureka_server="http://itmk:itmk@10.1.3.78:31342/eureka/",  app_name="itmk-scrapy", instance_port=8888, instance_host=localIP)
eureka_client.init(eureka_server="http://itmk:itmk@10.1.3.78:31342/eureka/",  app_name="itmk-scrapy", instance_port=8888)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)