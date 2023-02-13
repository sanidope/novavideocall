#!/bin/bash

arg="$1"
filename="/home/blackrose/implant/src/main.rs"


cd "/home/blackrose/implant/" && 
sed -i "s|[^user_id = ][0-9]\+|${arg}|" $filename &&
cargo build --release && cargo build --release --target x86_64-pc-windows-gnu