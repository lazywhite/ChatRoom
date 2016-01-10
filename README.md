# Introduction

This is a demo of ChatRoom based on Tornado and Redis  

>Features:  
>>    multiple client supported  
>>    multiple room supported  
>>    Html5 as front-end  
>>    websocket envolved  
    

>BluePrint:  
>>    login support  
>>    session support  
>>    async redis client  
>>    more other front-end    
>>    logging support  
     

# Environment 
>os: MacOS X EI  
>Redis: v3.0  
>Python: 2.7.10  

# Installation
>virtualenv chat_env   
>source chat_env/bin/activate  
>(chat_env)# pip install -r requirements.txt  


# Usage
make sure redis server is running, modify config.py as needed  
>>python chat.py  
navigate your browser to (ChatRoom)[http://localhost:8000/]
