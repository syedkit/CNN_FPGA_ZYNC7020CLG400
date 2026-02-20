# FPGA CNN Object Detection


## Institution

**Kangeyam Institute of Technology, Tamil Nadu, India**

---

## Team

**Team Lead**
S.I. Syed Arshad (B.E. Electronics and Communication Engineering – III Year)

**Team Members**

1. C. Pooja Sri (II – ECE)
2. N. Deepak (II – ECE)

---

## Project Description

This repository contains the complete design, development, and implementation of a **hardware-accelerated Convolutional Neural Network (CNN) based object detection system** on FPGA. The project focuses on real-time inference using FPGA acceleration to improve speed, reduce latency, and achieve energy-efficient deep learning.

The implementation is carried out on the **Xilinx Zynq-7020 SoC platform**, which combines ARM processors with FPGA programmable logic for heterogeneous computing.

**NOTE:-**(READ THIS FIRST)
READ THIS DOCUMENT FOR DATA METRIC ANALYSIS :-  https://github.com/syedkit/CNN_FPGA_ZYNC7020CLG400/blob/a9df090dc3cce925667c1bb10bcdf79404288151/PROJECT%20IMPLEMENTATION%20%E2%80%93%20DATA-DRIVEN%20STRUCTURED%20SUMMARY.docx
---

## Motivation

Modern AI and computer vision applications require:

* Low latency
* High performance
* Real-time processing
* Low power consumption
* Edge deployment

Traditional CPU and GPU solutions are not suitable for embedded edge systems due to power and cost constraints. FPGA provides a flexible and efficient alternative for deep learning acceleration.

---

## Objectives

The main goals of this project are:

* Design CNN accelerator using FPGA
* Implement convolution, activation, and pooling in hardware
* Perform hardware–software co-design
* Reduce inference time
* Compare CPU and FPGA performance
* Optimize hardware resource utilization
* Demonstrate real-time object detection

---

## System Architecture

The system is based on the Zynq SoC architecture:

### Processing System (PS)

* ARM Cortex-A9 processors
* Controls CNN hardware accelerator
* Handles preprocessing and postprocessing
* Runs PetaLinux

### Programmable Logic (PL)

* Implements CNN layers
* Accelerates computational operations
* Provides parallel processing

### Workflow

1. Image input is given
2. ARM performs preprocessing
3. CNN executed in FPGA
4. Output transferred back
5. Object detection result generated

---

## Hardware Platform

* Xilinx Zynq-7020 (CLG400 -1)
* AXI communication
* Heterogeneous computing

---

## Tools and Technologies

* Vivado
* Vitis
* Vitis HLS
* PetaLinux
* QEMU
* C/C++
* Python

---

## CNN Implementation

The CNN model includes:

* Convolution layer
* Depthwise convolution
* ReLU activation
* Pooling
* Fully connected layer

Optimizations performed:

* Parallelism
* Loop pipelining
* Memory optimization
* Hardware resource reduction

---

## Features

* Real-time object detection
* Hardware acceleration
* Low latency
* Energy efficient
* Embedded AI
* Scalable architecture

---

## Performance Metrics

* Latency
* Throughput
* Power
* Resource utilization

  * LUT
  * DSP
  * BRAM

Comparison is done with CPU-based implementation.

---

## Repository Structure

```
FPGA_CNN_OBJECT_DETECTION
│
├── hardware
│   ├── vivado
│   ├── bitstream
│
├── hls
│   ├── convolution
│   ├── activation
│   ├── pooling
│
├── software
│   ├── arm
│   ├── drivers
│
├── petalinux
│   ├── images
│
├── dataset
├── results
└── README.md
```

---

## Results

The FPGA-based implementation achieved:

* Reduced inference latency
* Higher throughput
* Low power consumption
* Efficient hardware utilization

The system demonstrates the feasibility of deploying deep learning models in embedded and edge platforms.

---

## Testing

The project was verified using:

* Simulation
* Hardware emulation (QEMU)
* Performance analysis

---

## Applications

* Smart surveillance
* Autonomous systems
* Robotics
* Industrial automation
* Healthcare imaging
* Edge AI

---

## Future Work

* Advanced CNN models
* Model quantization
* Real-time video
* Edge AI integration
* IoT connectivity

---

## Acknowledgement

We sincerely thank our faculty and mentors at **Kangeyam Institute of Technology** for their guidance and support. This work was carried out as part of research and academic development in embedded AI and hardware acceleration.

Special thanks to **Udhayakumar Sir** for continuous support and technical guidance.

---

## License

This project is intended for academic and research purposes only.

---

## Contact

For queries or collaboration:

* Email:syed7243016@gmail.com
* LinkedIn:www.linkedin.com/in/syedarshadrsg

---
## Attribution

If you use this project, please credit:

Author: S.I.SYED ARSHAD  
Source: https://github.com/syedkit/CNN_FPGA_ZYNC7020CLG400.git
If you find this project useful, consider giving it a star.
