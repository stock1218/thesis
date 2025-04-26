# Code Modernization Techniques Using Clang-Tidy for C23 Checked Arithmetic

This is a repository containing the deliverables for my Master's thesis. My thesis comprised of an exploration into a compiler-assisted
code modernization approach for rewriting code to use checked arithmetic. The deliverables for this project include a clang-tidy check
that will automatically match to statements that can be rewritten and suggest a rewrite. Other artifacts can be found in this repository including
logs from clang-tidy on several targets and rewrites of the str.h the Monocypher libraries.

# Repository Structure
Monocypher: This contains the rewritten Monocypher library
llvm-project: This is a submodule to my llvm fork that contains the clang-tidy check
source: the LaTex source for my thesis
str: the rewritten str.h string library
tests: contains the test script and logs from clang-tidy for str.h, Monocypher, and Binutils

# Building the Check

To build the clang-tidy check, follow the instructions for building clang [here](https://clang.llvm.org/extra/clang-tidy/Contributing.html).

The specific commands I used from the main LLVM directory is `cmake -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra" -DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBRARIES=OFF -DLLVM_BUILD_EXAMPLES=ON -G "Visual Studio 17 2022" -A x64 -Thost=x64 ..\llvm`

This will create an `LLVM.sln` file you can open using Visual Studio Code.

# Resources
# Checked C
[https://github.com/jart/jtckdint](https://github.com/jart/jtckdint)
[https://gitlab.com/Kamcuk/ckd](https://gitlab.com/Kamcuk/ckd)  
[https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Integer-Overflow-Builtins.html](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Integer-Overflow-Builtins.html)
[https://clang.llvm.org/docs/LanguageExtensions.html#checked-arithmetic-builtins](https://clang.llvm.org/docs/LanguageExtensions.html#checked-arithmetic-builtins)


# Integer Overflow
(https://en.wikipedia.org/wiki/Integer_overflow)[https://en.wikipedia.org/wiki/Integer_overflow]

# C23
https://gustedt.gitlabpages.inria.fr/c23-library/
towards integer safety: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2543.pdf

standard for c23: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf
	- behavior definitions in 3.5
rational for C99 standard: https://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf
	- relevant section is page 37
 - Ritchie article on creating C: https://archive.org/details/DevelopmentOfC/page/6/mode/2up
 - stuff in here about interesting overflow bugs in prior work: https://users.cs.utah.edu/~regehr/papers/overflow12.pdf
 - standardizing things: https://en.wikipedia.org/wiki/ANSI_C#:~:text=ANSI%20C%2C%20ISO%20C%2C%20and%20Standard%20C,as%20doing%20so%20helps%20portability%20between%20compilers.
 - wtf there's an official website? https://www.c-language.org/faq

# Clang and LLVM
https://discourse.llvm.org/t/reading-and-attaching-comments-to-clang-ast/47796
https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/
https://stackoverflow.com/questions/46692246/source-to-source-transformation-with-clang-state-of-the-art
https://clang.llvm.org/docs/ClangTransformerTutorial.html
Talk about AST: https://www.youtube.com/watch?v=VqCkCDFLSsc
https://jonasdevlieghere.com/post/understanding-the-clang-ast/
How clang makes error messages: https://clang.llvm.org/diagnostics.html
Clang plugins: https://clang.llvm.org/docs/ClangPlugins.html
LibTooling: https://clang.llvm.org/docs/LibTooling.html
CMU class slides: https://www.cs.cmu.edu/afs/cs/academic/class/15745-s15/public/lectures/L6-LLVM2-1up.pdf
API stuff: https://llvm.org/docs/ProgrammersManual.html#the-isa-cast-and-dyn-cast-templates
Building plugin on Windows: https://discourse.llvm.org/t/clang-wont-run-example-plugins-on-windows/57231/2
old post on building PrintFunctionNames: https://discourse.llvm.org/t/building-the-example-plugin-printfunctionnames/53604
Video on development on windows: https://www.youtube.com/watch?v=zlD2MpU7XIw

# C++
https://www.boost.org/doc/libs/1_76_0/libs/safe_numerics/doc/html/introduction.html

# Microsoft
[https://stackoverflow.com/questions/69565333/are-there-overflow-check-math-functions-for-msvc](https://stackoverflow.com/questions/69565333/are-there-overflow-check-math-functions-for-msvc)  
[https://learn.microsoft.com/en-us/cpp/safeint/safeint-library?view=msvc-170](https://learn.microsoft.com/en-us/cpp/safeint/safeint-library?view=msvc-170)  
[https://learn.microsoft.com/en-us/windows/win32/api/intsafe/](https://learn.microsoft.com/en-us/windows/win32/api/intsafe/)  
[https://threadreaderapp.com/thread/1799457232607985698.html](https://threadreaderapp.com/thread/1799457232607985698.html)

# Other Languages

# Academic Papers
[[Holistic Control-Flow Protection on Real-Time Embedded Systems with Kage]]
[[InversOS Efficient Control-Flow Protection for AArch64 Applications with Privilege Inversion]]

