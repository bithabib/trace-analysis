# blkparse README

## Overview
The `blkparse` utility is used to combine streams of events for various block devices and CPUs, providing a formatted output of the event information. It takes the machine-readable output of the `blktrace` utility and converts it into a human-readable form.

## Usage
### Running blkparse
By default, `blkparse` expects to run in a post-processing mode, where trace events have been saved by a previous run of `blktrace`. It combines event streams and dumps formatted data. It can also be run in live mode concurrently with `blktrace` by specifying `-i -` to `blkparse` and combining it with the live option for `blktrace`.

### Options
- `-A hex-mask`, `--set-mask=hex-mask`: Set filter mask to hex-mask.
- `-a mask`, `--act-mask=mask`: Add mask to current filter.
- `-D dir`, `--input-directory=dir`: Prepend dir to input file names.
- `-b batch`, `--batch={batch}`: Standard input read batching.
- `-i file`, `--input=file`: Specifies base name for input files. Default is `device.blktrace.cpu`.
- `-F typ,fmt`, `--format=typ,fmt`, `-f fmt`, `--format-spec=fmt`: Sets output format. Allows specifying a format for all events (`-f`) or for a specific event type (`-F`).
- `-M`, `--no-msgs`: Stop messages from being output to the file when using the `-d` option.
- `-h`, `--hash-by-name`: Hash processes by name, not by PID.
- `-o file`, `--output=file`: Output file.
- `-O`, `--no-text-output`: Do not produce text output, used for binary (`-d`) only.
- `-d file`, `--dump-binary=file`: Binary output file.
- `-q`, `--quiet`: Quiet mode.
- `-s`, `--per-program-stats`: Displays data sorted by program.
- `-t`, `--track-ios`: Display time deltas per IO.
- `-w span`, `--stopwatch=span`: Display traces for the specified span.

### Trace Actions
The following trace actions are recognized:
- `C`: Complete
- `D`: Issued
- `I`: Inserted
- `Q`: Queued
- `B`: Bounced
- `M`: Back merge
- `F`: Front merge
- `G`: Get request
- `S`: Sleep
- `P`: Plug
- `U`: Unplug
- `T`: Unplug due to timer
- `X`: Split
- `A`: Remap


### RWBS Description or Operation Type Description
The RWBS field is a small string that provides information about the type of operation performed. It contains at least one character, where:
- 'R': Indicates a read operation.
- 'W': Indicates a write operation.
- 'D': Indicates a block discard operation.

Additionally, the RWBS field may optionally include:
- 'B': Represents barrier operations.
- 'S': Represents synchronous operations.

### Output Description and Formatting
The output from `blkparse` can be tailored for specific use, including field display width and alignment. Available fields include action, CPU ID, command, RWBS field, device major/minor, error value, minor/major number of event's device, number of blocks/bytes, process ID, sequence numbers, sector number, time stamp, elapsed time, payload, and more.

## Authors
`blkparse` was written by Jens Axboe, Alan D. Brunelle, and Nathan Scott. This manual page was created from the `blktrace` documentation by Bas Zoetekouw.

## Reporting Bugs
Report bugs to [linux-btrace@vger.kernel.org](mailto:linux-btrace@vger.kernel.org).

## Copyright and License
`blkparse` is free software distributed under the terms of the GNU General Public License. See the [license file](LICENSE) for details.
