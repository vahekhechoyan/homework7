def html_tag(tag):
    def inner(content):
        return f"<{tag}>{content}</{tag}>"
    return inner

p_tag = html_tag("p")
div_tag = html_tag("div")

print(p_tag("This is a paragraph."))  
print(div_tag("This is a div."))