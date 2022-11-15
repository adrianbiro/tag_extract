# Extract some coordinates

[link](https://stackoverflow.com/questions/22898145/how-to-extract-text-and-text-coordinates-from-a-pdf-file/69151177#69151177)

```bash
$ docker pull biroadrian/extract:0.3
$ docker run --rm -v $(pwd):/app -w /app extract:0.3 <file.pdf>
```
or
```bash
docker run --rm -v $(pwd):/fall -w /fall biroadrian/extract:0.3 <file.pdf>
```
```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python3 tagextract.py <file.pdf>
$ deactivate
```

