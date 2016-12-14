export KALDI_ROOT=`pwd`/../../..
[ -f $KALDI_ROOT/tools/env.sh ] && . $KALDI_ROOT/tools/env.sh
export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh

# VoxForge data will be stored in:
export DATA_ROOT="/Volumes/Seagate/Seagate_Dashboard/kaldi/egs/voxforge/s5/lang"
export DATA_ROOT_ENG="/Volumes/Seagate/Seagate_Dashboard/kaldi/egs/voxforge/s5/lang/eng"    # e.g. something like /media/secondary/voxforge
export DATA_ROOT_FRN="/Volumes/Seagate/Seagate_Dashboard/kaldi/egs/voxforge/s5/lang/frn"

if [ -z $DATA_ROOT ]; then
  echo "You need to set \"DATA_ROOT\" variable in path.sh to point to the directory to host VoxForge's data"
  exit 1
fi

# Make sure that MITLM shared libs are found by the dynamic linker/loader
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/tools/mitlm-svn/lib

# Needed for "correct" sorting
export LC_ALL=C
