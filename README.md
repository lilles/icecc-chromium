# Building chromium on an icecc cluster

## Prerequisites

  - A chromium checkout on a Linux computer
  - ccache
  - icecc version >= 1.1rc2.
  - A functioning icecc cluster and a running iceccd on the local computer

## Setup

  - Add repo root directory to $PATH
  - source ccache-env
  - Add custom hook to .gclient. See documentation in icecc-create-env.py
  - Run gclient runhooks

## Usage

Build with icecc-ninja instead of ninja. For instance:

```icecc-ninja -j64 -C out/Release blink_tests```

## Issues

Using clang plugins does not work. They are disabled in icecc.gni which means
that e.g. some oilpan errors will go unnoticed.

From time to time there are compile errors which only happen when distributed
with icecc. I have seen at least the avx512 issue mentioned in [1]. A workaround
for that without messing with local patches is to run ninja instead of
icecc-ninja for the problematic target(s).

\[1\] [https://github.com/ds-hwang/wiki/wiki/Set-up-icecc-with-heterogeneous-env]
(https://github.com/ds-hwang/wiki/wiki/Set-up-icecc-with-heterogeneous-env)

## License

See LICENSE file
