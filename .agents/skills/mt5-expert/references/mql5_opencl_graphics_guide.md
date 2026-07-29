# MQL5 OpenCL GPU Acceleration & CCanvas Reference Guide

## 1. OpenCL Parallel Computing Functions
- `CLContextCreate(ENUM_CL_DEVICE_TYPE device_type)`: Creates GPU context (`CL_USE_GPU_ONLY` or `CL_USE_ANY`).
- `CLProgramCreate(long context, string code)`: Compiles OpenCL C kernel source code.
- `CLKernelCreate(long program, string kernel_name)`: Obtains handle for OpenCL kernel function.
- `CLSetKernelArg(long kernel, uint arg_index, const void &arg_value)`: Sets kernel parameters.
- `CLBufferCreate(long context, uint size, uint flags)`: Allocates memory buffer on GPU.
- `CLExecute(long kernel, uint work_dim, const uint &work_offset[], const uint &work_size[])`: Launches parallel GPU execution.

---

## 2. CCanvas & Custom Graphics
Used to render custom visual dashboards, buttons, matrices, and charts directly onto MT5 charts.

```mql5
#include <Canvas\Canvas.mqh>

CCanvas extCanvas;

int InitDashboard(int x, int y, int width, int height)
{
   if(!extCanvas.CreateBitmapLabel("MyDashboard", x, y, width, height, COLOR_FORMAT_ARGB_NORMALIZE))
      return(INIT_FAILED);

   extCanvas.Erase(ColorToARGB(clrBlack, 200));
   extCanvas.TextOut(10, 10, "MT5 EXPERT V2 DASHBOARD", ColorToARGB(clrLimeGreen), FONT_BASE);
   extCanvas.Update();

   return(INIT_SUCCEEDED);
}

void DestroyDashboard()
{
   extCanvas.Destroy();
}
```
