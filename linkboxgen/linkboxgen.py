import json;

def main():
    with open("linkbox.json","r",encoding="utf8") as jfile:
        data=json.load(jfile);

    with open("linkbox-output.html","w",encoding="utf8") as ofile:
        for i,x in enumerate(data["links"]):
            ofile.write(genLinkBox(x,data["img"][i],data["text"][i]));


def genLinkBox(link,img,title):
    return '''<link-box href="{}" img="{}">
    {}
    </link-box>\n\n'''.format(link,img,title);

main();