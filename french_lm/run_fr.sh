# mkdir dict
# python dictionary.py

# echo "SIL" > dict/silence_phones.txt
# echo "SIL" > dict/optional_silence.txt
# mv dict/phones.txt dict/nonsilence_phones.txt
# cp dict/lexicon.txt dict/lexicon_words.txt
# echo "<SIL> SIL" >> dict/lexicon.txt

utils/prepare_lang.sh --position-dependent-phones false dict "<SIL>" dict/tmp data/lang

#python prep_data.py

FILES="test
train"

for x in $FOLDERS 
do
	steps/make_mfcc.sh data/$x exp/make_mfcc/$x
	steps/compute_cmvn_stats.sh data/$x exp/make_mfcc/$x
	steps/train_mono.sh --nj 1 --cmd utils/run.pl data/$x data/lang exp/mono/$x
done

utils/make_lexicon_fst.pl dict/lexicon.txt > dict/lexicon.fst.txt
tools/openfst/bin/fstcompile --isymbols=data/lang/phones.txt --osymbols=data/lang/words.txt \
    dict/lexicon.fst.txt data/lang/G.fst

utils/mkgraph.sh --mono data/lang exp/mono exp/mono/

# # Monophone decoding
#utils/mkgraph.sh --mono data/lang exp/mono exp/mono/graph_tgpr
# # note: local/decode.sh calls the command line once for each
# # test, and afterwards averages the WERs into (in this case
# # exp/mono/decode/
# steps/decode.sh --config conf/decode.config --nj $njobs --cmd "$decode_cmd" \
#   exp/mono/graph data/test exp/mono/decode

# # # Get alignments from monophone system.
# steps/align_si.sh --nj $njobs --cmd "$train_cmd" \
#   data/train data/lang exp/mono exp/mono_ali

# # # train tri1 [first triphone pass]
# steps/train_deltas.sh --cmd "$train_cmd" \
#   2000 11000 data/train data/lang exp/mono_ali exp/tri1




# #number of parallel jobs to be started
# njobs=2

# #number of randomly selected sepakers to be put in the test set
# nspk_test=20

# #test-time language model order

# #word position dependent phones
# pos_dep_phones=true

# selected=${DATA_ROOT_FRN}/selected/extracted

# #mapping anonymous speakers to unique IDs
# local/voxforge_map_anonymous.sh ${selected}

# #initial normalization of the data
# local/voxforge_data_prep.sh --nspk_test 