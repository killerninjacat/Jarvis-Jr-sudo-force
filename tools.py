import typer
import sys
from selectolax.parser import HTMLParser 
import requests
from rich import print
from pydantic import BaseModel

app = typer.Typer()

USERS : dict[str, str] = {"sid":"123", "delta":"234"}
'''
@app.command()
def hello():
    print("Hello Sid what do you want to do today :)")

    
@app.command()
def goodbye():
    print("Have a good day Sid/nHope to see you again")
'''
@app.command()
def unlock(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True),
):
    if USERS.get(username) != password:
        print("[red] incorrect uername or pswd[/red]")
        raise typer.Exit(code=1)
    print(f"[green] Welcome {username} :)[/green]")
    
    

if __name__ == "__main__":
    app()
    


'''
class Asin(BaseModel):
    id: str

class Item(BaseModel):
    asin: Asin
    price: str

@app.command()
def getBrowser(asin: str):
    new_asin = Asin(id =asin)
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"  }
    resp = requests.get("https://www.amazon.in/" + new_asin.id, headers= headers)
    html = HTMLParser(resp.text)
    new_item = Item(asin= new_asin, price = html.css_first("spam.a-offscreen").text().strip())
    print(new_item)

'''
