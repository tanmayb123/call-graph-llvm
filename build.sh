rm -rf build
mkdir build && cd build && cmake .. && make && echo $(pwd) && cd .. && echo "complete"
