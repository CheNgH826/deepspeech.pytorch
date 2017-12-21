import argparse
import librosa
import numpy as np
import spectrogram as spg
import os
class Store_as_array(argparse._StoreAction):
    def __call__(self, parser, namespace, values, option_string=None):
        values = np.array(values)
        return super().__call__(parser, namespace, values, option_string)

def argparser():
	parser = argparse.ArgumentParser("Mini program for audio conversion")
	parser.add_argument('--wav', type=str, required=False)
	parser.add_argument('--sr', type=int, default=16000)
	parser.add_argument('--outdir', type=str, default='output')
	parser.add_argument('--spec',type=str, required=True)
	#parser.add_argument('--figsize', type=tuple, default=(12, 8))
	args = parser.parse_args()
	return args



def spec2audio(spectrogram):
	
	soundarray = spg.spectrogram2wav(spectrogram)
	librosa.output.write_wav(outdir+'/converted-{0}'.format(wav_file), soundarray, sr)

if __name__ == "__main__":
	args = argparser()

	wav_file 	= args.wav	# audio file
	sr 			= args.sr 		# sample rate
	spec	    = np.load(args.spec)
	outdir		= args.outdir
	#figsize		= args.figsize
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	
	spec2audio(spec)

    
