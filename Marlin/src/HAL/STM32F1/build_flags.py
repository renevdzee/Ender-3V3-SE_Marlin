from __future__ import print_function
import sys

# Removed -mcpu and -mthumb because they are set by platformio/framework
# so can also be used for stm32f3 cortex-m4 (needs platformio-build-stm32f3.py)
# also, LINKFLAGS below does nothing ...

#dynamic build flags for generic compile options
if __name__ == "__main__":
  args = " ".join([ "-std=gnu++14",
                    "-Os",

                    "-fsigned-char",
                    "-fno-move-loop-invariants",
                    "-fno-strict-aliasing",

                    "--specs=nano.specs",
                    "--specs=nosys.specs",

                    "-IMarlin/src/HAL/STM32F1",

                    "-MMD",
                    "-MP",
                    "-DTARGET_STM32F1"
                  ])

  for i in range(1, len(sys.argv)):
    args += " " + sys.argv[i]

  print(args)

# extra script for linker options
else:
  from SCons.Script import DefaultEnvironment
  env = DefaultEnvironment()
  env.Append(
      ARFLAGS=["rcs"],

      ASFLAGS=["-x", "assembler-with-cpp"],

      CXXFLAGS=[
          "-fabi-version=0",
          "-fno-use-cxa-atexit",
          "-fno-threadsafe-statics"
      ],
      LINKFLAGS=[
          "-Os",
          "-ffreestanding",
          "--specs=nano.specs",
          "--specs=nosys.specs",
          "-u_printf_float",
      ],
  )
