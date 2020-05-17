# CUDA

### 計算順序

まず、CPU が変数を初期化し、その変数を GPU にデータ転送を行う  
その後、GPU に処理が移り、CUDA カーネルで実行、同期、終わったら CPU にデータ転送を行う  
まとめると、CPU から GPU へデータを転送し、CUDA カーネルを実行する流れ

### 単位

- `GRID`

  - 一番大きい単位
  - いくつかの `BLOCK` が集まって`GRID` が出来上がる

- `BLOCK`

  - `GRID` の中にある
  - x, y, z 座標を持っている
  - いくつかの `THREAD` が集まって一つの `BLOCK` が出来上がる

- `THREAD`
  - `BLOCK` の中にある
  - x, y, z 座標を待っている
  - GPU 並列する際に計算を担う

#### GRID

GRID は BLOCK で構成されており、GRID のサイズは BLOCK の個数から決まる  
これを gridDim という

例えばブロックが、`x 軸に 3`、`y 軸に 2`、`z 軸に 1` のとき、GRID のサイズは以下のようになる

```python
gridDim.x = 3
gridDim.y = 2
gridDim.z = 1
```

#### BLOCK

BLOCK は THREAD で構成されており、BLOCK のサイズは THREAD の個数から決まる  
これを blockDim という

また、BLOCK は GRID の中に複数あるので、座標が割り振られている  
これを blockId という

#### THREAD

THREAD は座標のみ割り振られている

### WARP

THREAD 全体が同時に計算を始めるのではなく、<strong>WARP 単位で同時に動く</strong>

WARP 自体は、32 個の THREAD が集まったもの

一つの WARP の THREAD 全体が同一の命令を実行することを、 `SIMT(Single Instruction Multiple Thread)` という

### メモリ構造

GPU のメモリ構造は CPU と異なる  
大まかに二つに分けられる

- オンチップメモリ
  - メモリが CUDA Core に近い
  - 容量は小さい
  - アクセスは速い
- オフチップメモリ
  - メモリが CUDA Core から遠い
  - 容量は大きい
  - アクセスが遅い

### インストール

Python で CUDA を取り扱うため、CUDA を Python でラッピングしている `pycuda` ライブラリを用いる

```
$ pip3 install pycuda
```

### Hello World

```python
import numpy as np
# GPU ARRAY
import pycuda.gpuarray as gpuarray
# Define function for GPU Kernel
from pycuda.elementwise import ElementwiseKernel
# Just import and Automate GPU Initialize
import pycuda.autoinit

# Define What to do
plus_one_kernel = ElementwiseKernel(
  # Args
  "int *y, int *x",
  # Process
  "y[i] = x[i] + 1",
  # Function name
  "plus_one"
)

# [0, 1, ... , 8, 9]
x = np.arrange(10, dtype=np.int32)
# Send cpu memory to gpu
x_gpu = gpuarray.to_gpu(x)
y_gpu = gpuarray.zero(10, dtype=np.int32)

# Execute
plus_one_kernel(y_gpu, x_gpu)

# Get the result from gpu
y_gpu.get()
```
