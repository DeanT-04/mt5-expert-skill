# MQL5 ONNX Machine Learning Integration Reference Guide

## 1. Native MQL5 ONNX Functions & API
MetaTrader 5 supports native ONNX (Open Neural Network Exchange) model inference:

- `OnnxCreate(const string filename, uint flags)`: Loads ONNX model file from `MQL5\Files\`.
- `OnnxCreateFromBuffer(const uchar &buffer[], uint flags)`: Loads ONNX model from byte buffer.
- `OnnxSetInputShape(long handle, ulong index, const long &shape[])`: Sets tensor dimensions.
- `OnnxSetOutputShape(long handle, ulong index, const long &shape[])`: Sets expected output dimensions.
- `OnnxRun(long handle, uint flags, const void &inputs[], void &outputs[])`: Runs inference.
- `OnnxRelease(long handle)`: Frees model session memory.

---

## 2. Standard ONNX Model Execution Template

```mql5
//+------------------------------------------------------------------+
//| ONNX Machine Learning Inference Template                         |
//+------------------------------------------------------------------+
#property copyright "Copyright 2026, MetaQuotes Ltd."
#property version   "1.00"

long extModelHandle = INVALID_HANDLE;

int OnInit()
{
   // 1. Create ONNX session from MQL5\Files\model.onnx
   extModelHandle = OnnxCreate("model.onnx", ONNX_DEFAULT);
   if(extModelHandle == INVALID_HANDLE)
   {
      PrintFormat("Failed to load ONNX model. Error: %d", GetLastError());
      return(INIT_FAILED);
   }

   // 2. Set input shape [batch_size=1, features=10]
   long inputShape[] = {1, 10};
   if(!OnnxSetInputShape(extModelHandle, 0, inputShape))
   {
      Print("Failed to set ONNX input shape");
      return(INIT_FAILED);
   }

   // 3. Set output shape [batch_size=1, classes=2]
   long outputShape[] = {1, 2};
   if(!OnnxSetOutputShape(extModelHandle, 0, outputShape))
   {
      Print("Failed to set ONNX output shape");
      return(INIT_FAILED);
   }

   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason)
{
   if(extModelHandle != INVALID_HANDLE)
   {
      OnnxRelease(extModelHandle);
      extModelHandle = INVALID_HANDLE;
   }
}

bool PredictSignal(const float &inputs[], float &predictions[])
{
   if(extModelHandle == INVALID_HANDLE) return false;
   return OnnxRun(extModelHandle, ONNX_NO_CONVERSION, inputs, predictions);
}
```
