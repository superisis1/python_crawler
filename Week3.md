## BeautifulSoup
BeautifulSoup(뷰티풀솝)은 데이터를 추출하는데 필요한 기능이 들어있는 라이브러리 입니다.
* 반도체공장(모래) = BeautifulSoup(html)

## 라이브러리(library)
라이브러리(library)는 도서관이라는 뜻입니다. 책이 여러권 있는 곳이 도서관인데 여러가지 기능들이 있는 코드 묶음을 라이브러리라고 합니다.
* 많이 사용하는 기능들을 다른 사람 또는 회사가 만들어서 올려놓은 것입니다.
* 라이브러리는 import를 해서 사용 합니다.
* 내장 라이브러리와 외장 라이브러리가 있습니다.
* 내장 라이브러리는 import해서 사용하고 외장 라이브러리는 설치한 후 import해서 사용합니다.

## 라이브러리 설치 하는 방법
* Settings(Preferance) -> interpreter검색
* +를 누르고 설치하고 싶은 라이브러리 검색 ex)bs4, numpy 등   


###  BeautifulSoup 사용법
```python
import bs4
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
```

위 코드를 그냥 실행 하면 모듈이 없다는 에러가 납니다.
그래서 bs4를 설치 해야 합니다.

### 크롤링이란?
인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
* 라이브러리 : urlopen

### 파싱이란?
크롤링한 데이터에서 값을 뽑아내는 것
* 라이브러리:bs4 BeautifulSoup 뷰티풀솝


### 태그란?
html문서를 표현 할 때 쓰는 화면 구성을 하는 표시들.
```html
<html>, <div>, <ul>, <li>, <a>, <span> 등이 있다.
```

### ul태그 뽑아내기
위 소스코드는 <div>태그를 뽑아내는 예제였습니다. 이 예제는 ul태그를 뽑아내는 예제 입니다.

모든 데이터는 태그 안에 들어있습니다.

예를 들면 뉴스 기사 들은 아래와 같이 데이터가 들어가 있습니다.

```html
<ul>
	<li>000가 000를 했다</li>
	<li>111가 222를 했다</li>
</ul>
```
웹에 표시되는 데이터는 태그로 감싸져 있습니다.

```json
[
	{"title":"000가 000를 했다"},
	{"title":"111가 222를 했다"}
]
```
이러한 리스트 구조와 비슷합니다. 이건 json이라고 하는데 뒤에 배웁니다. 모양이 비슷하기 때문에 넣어놓았습니다.

"""따옴표 3개로 감싸주면 변수에 여러줄을 넣을 수 있습니다.
```python
import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bsObj.find("ul")
print(ul)

```

### 데이터 받아서 파싱하기
네이버에서 맨 오른쪽 위에 있는 '네이버를 시작페이지로'이 글자를 파싱 하는 코드입니다.
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a.text)
```
