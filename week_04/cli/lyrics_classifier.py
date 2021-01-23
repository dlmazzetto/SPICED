from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import sys
import argparse

ARTIST_1 = 'Spice Girls'
ARTIST_2 = 'Beatles'

TEXT_CORPUS = ['last time that we had this conversation',
               'if you wanna be my lover',
               'spice up your life',
               'ill tell you what i want',
               'what i really really want',
               'you cant do nothing for me baby',
               'we all live in a yellow submarine',
               'all you need is love',
               'eleanor rigby puts on a face that she keeps in a jar by the door',
               'yesterday all my troubles seemed so far away',
               'lucy in the sky with diamonds',
               'i am the walrus']

LABELS = [ARTIST_1] * 6 + [ARTIST_2] * 6


def train_model(text, labels):
    """
    Trains a scikit-learn classification model on text.

    Parameters
    ----------
    text : list
    labels : list

    Returns
    -------
    model : Trained scikit-learn model.

    """

    cv = CountVectorizer(stop_words='english')
    tf = TfidfTransformer()
    rf = RandomForestClassifier()
    model = make_pipeline(cv, tf, rf)
    model.fit(text, labels)

    return model


def predict(model, new_text):
    """
    Takes the pre-trained model pipeline and predicts new artist based on unseen text.

    Parameters
    ----------
    model : Trained scikit-learn model pipeline.
    new_text : str

    Returns
    ---------
    prediction : str

    """
    new_text = [new_text]
    prediction = model.predict(new_text)

    return prediction[0]


if __name__ == '__main__':
    # Whatever happens after this line, execute it when running "python lyrics_classifier.py"
    # and DO NOT execute these lines of code if things from this script are imported from other scripts.

    model = train_model(TEXT_CORPUS, LABELS)
    # user_input = input('Please Enter Some Text: ') OPTION A!!!
    # user_input = sys.argv[1] OPTION B!!!

    parser = argparse.ArgumentParser(description='Lyrics Classifier')
    parser.add_argument('-t', '--text', type=str, help='Enter some new text')
    args = parser.parse_args()

    prediction = predict(model, args.text)
    print('Here is your prediction!')
    print(prediction)
