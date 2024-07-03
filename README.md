# How to detect an illegal mining site

Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate
```
Install all the required packages
```bash
pip install -r requirements. txt
```
To change the model used to predict, go to predict.py and change the path to the desired model
```python
model = YOLO("./runs/detect/train/weights/best.pt")
```
With everything set up correctly, execute predict.py

# How to train a new model

Create a .yaml file called data_custom.yaml with the nescessary paths to your dataset.
The project uses the following dataset
<a href="https://drive.google.com/file/d/1OJDly_end-WCl0a2kRNXlpt7HgXsgZKX/view?usp=sharing">mining-dataset</a>

```yaml
train: /path/to/mining-dataset/train
val: /path/to/mining-dataset/valid

names:
  0: illegal_mining
```
With the proper paths added, simply execute train.py with the activated virtual environment


# References

<div class="csl-bib-body">
  <div class="csl-entry">Labbe, N. (2021). <i>Detecting illegal gold mining sites in the Amazon forest : Using Deep Learning to Classify Satellites Images</i> (Dissertation). Retrieved from https://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-307579</div>
</div>
