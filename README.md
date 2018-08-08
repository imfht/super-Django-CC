## About
* Designed by [fht.im](https://fht.im)
* Data from [http://commoncrawl.org/](http://commoncrawl.org/)

## Online site
Visit [url.fht.im](http://url.fht.im)

## Preview
![](http://ww1.sinaimg.cn/large/0062TDWsgy1fu2mau7gf5j31rq0twaeq.jpg)

## Build
### install from source
make sure you've installed python3 and virtualenv.
#### 1. create virtual work directory and active it.

```bash
virtualenv venv -p /usr/bin/python3 # or use which python find your python3 path
source venv/bin/active
```
#### 2. install requirements

```bash
cd super-Django-CC && pip install -r requirements.txt
``` 
#### 3. Run it 
```python
python manager.py runserver 127.0.0.1:8001
```
Then visit localhost:8001 you will get a preview.

## build by docker
get the code && docker build && docker run 
```bash
git clone https://github.com/imfht/super-Django-CC && cd super-Django-CC && docker build . -t super_django_cc 
```
Run it 
```bash
docker run -p8001:8001 -d super_django_cc
```
Then visit localhost:8001 you will get a preview.

## Q&A
1. What is this?   
    show how many urls and websites was exposed to web crawls. 
2. Why I get very few result for my site?    
    all the data is from commoncrawl.org, throght it crawled loooots of pages in the internet. But crawl all website's page is impossable.
3. TOS & Rate limiting    
    TOS of the site as same as [http://commoncrawl.org/terms-of-use/](http://commoncrawl.org/terms-of-use/). Respectful robots is welcome. Respectful means the max rate is 5 req/s. If you wanner increase it please use commoncrawl's open data or contact me.