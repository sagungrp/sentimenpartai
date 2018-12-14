   # Installation

    clone repo
    cd.. venv
    pip install virtualenv
windows
    activate.bat
Linux
    source activate

Make sure virtual environment is created, check so your command prompt look like this

    (venv) $ _
Then continue with
    
    pip install -r req.txt
    python main.py
    
Then open http://127.0.0.1:5000 in your browser


## About

**RULE-BASED SENTIMENT ANALYSIS ATAS PARTAI PESERTA PEMILU 2019 MELALUI TWITTER**

The algorithm makes three passes for every given tweet

- **First scan:** Negation keyword('tidak', 'bukan',...)
	For every 3 opinion keywords immediately proceding the negation, add their score by _(- (keyword*2))_

- **Second scan:** opinion keywords ('keren','jelek','hebat','kampungan',...)

- **Third scan:** Opposite conjunctions('namun', 'tetapi, 'tapi') Modify the score of the tweet by multiplying it with a constant

The total score is the sum of all three scan. If the score is above 0, the tweet is labeled as positive; if the score is below zero, it is labeled as negative; if the score is 0, it is labelled as neutral.


## References

_List of Opinion Words (positive/negative) in Bahasa Indonesia._ _Originated by Liu's Opinion Words list with modification/translation to Indonesia._

_Wahid, D. H., & Azhari, S. N. (2016). Peringkasan Sentimen Esktraktif di Twitter Menggunakan Hybrid TF-IDF dan Cosine Similarity. IJCCS (Indonesian Journal of Computing and Cybernetics Systems), 10(2), 207-218._

_Liu, Bing, Hu, Minqing, and Cheng, Junsheng (2005). Opinion Observer: Analyzing and Comparing Opinions on the Web. Proceedings of the 14th International World Wide Web Conference (WWW-2005), May 10-14, Chiba, Japan._

_Kan, D. (2011). Rule-based approach to sentiment analysis. Russian Information Retrieval Evaluation Seminar 2011._
