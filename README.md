# Extract some coordinates

[link](https://stackoverflow.com/questions/22898145/how-to-extract-text-and-text-coordinates-from-a-pdf-file/69151177#69151177)


[docker](https://hub.docker.com/r/biroadrian/extract)
```bash
$ docker pull biroadrian/extract:0.4
$ docker run --rm -v $(pwd):/fall -w /fall biroadrian/extract:0.4 <file.pdf>
```
powershell
```pwsh
PS C:\> docker run --rm -v ${pwd}:/fall -w /fall biroadrian/extract:0.4 t1.pdf
```
```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python3 tagextract.py <file.pdf>
$ deactivate
```

