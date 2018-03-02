from ktext.preprocess import processor
import dill as dpickle
import numpy as np


class TextToNumber:

    @staticmethod
    def create_number_vector(raw_text_array, max_uniqie_words_size=8000, padding_maxlen=70, padding_position='post',
                             output_file='nummerical_text'):
        body_pp = processor(keep_n=max_uniqie_words_size, padding_maxlen=padding_maxlen, padding=padding_position)
        vecs = body_pp.fit_transform(raw_text_array)

        if output_file is not None:
            # Save the preprocessor
            with open(output_file + '.dpkl', 'wb') as f:
                dpickle.dump(body_pp, f)

            # Save the processed data
            np.save(output_file + '.npy', vecs)

        return vecs
