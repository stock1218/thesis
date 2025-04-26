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
## Checked C
[jtckdint (GitHub)](https://github.com/jart/jtckdint)

[ckd (GitLab)](https://gitlab.com/Kamcuk/ckd)

[Integer Overflow Builtins (GCC 14.2.0 Documentation)](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Integer-Overflow-Builtins.html)

[Checked Arithmetic Builtins (Clang Language Extensions)](https://clang.llvm.org/docs/LanguageExtensions.html#checked-arithmetic-builtins)



## Integer Overflow
[Wikipedia page](https://en.wikipedia.org/wiki/Integer_overflow)

[Thread about overflow and integer safety (ThreadReader)](https://threadreaderapp.com/thread/1799457232607985698.html)

[Paper on integer overflow bugs](https://users.cs.utah.edu/~regehr/papers/overflow12.pdf)

## C23
[C23 Library](https://gustedt.gitlabpages.inria.fr/c23-library/)

[Towards Integer Safety (WG14 N2543)](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2543.pdf)

[Standard for C23 (WG14 N3220)](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf) — behavior definitions in section 3.5

[Rationale for the C99 Standard (C99RationaleV5.10.pdf)](https://www.open-std.org/jtc1/sc22/wg14/www/C99RationaleV5.10.pdf) — relevant section is page 37

[Ritchie article on creating C (Development of C)](https://archive.org/details/DevelopmentOfC/page/6/mode/2up)

[Wikipedia article on ANSI C and standardization](https://en.wikipedia.org/wiki/ANSI_C#:~:text=ANSI%20C%2C%20ISO%20C%2C%20and%20Standard%20C,as%20doing%20so%20helps%20portability%20between%20compilers.)

[Official C Language FAQ website](https://www.c-language.org/faq)


## Clang and LLVM
[Reading and attaching comments to Clang AST](https://discourse.llvm.org/t/reading-and-attaching-comments-to-clang-ast/47796)

[My First Language Frontend tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/)

[Source-to-source transformation with Clang - StackOverflow](https://stackoverflow.com/questions/46692246/source-to-source-transformation-with-clang-state-of-the-art)

[Clang Transformer Tutorial](https://clang.llvm.org/docs/ClangTransformerTutorial.html)

[Talk about AST (YouTube)](https://www.youtube.com/watch?v=VqCkCDFLSsc)

[Understanding the Clang AST](https://jonasdevlieghere.com/post/understanding-the-clang-ast/)

[How Clang makes error messages](https://clang.llvm.org/diagnostics.html)

[Clang plugins](https://clang.llvm.org/docs/ClangPlugins.html)

[LibTooling](https://clang.llvm.org/docs/LibTooling.html)

[CMU class slides on LLVM](https://www.cs.cmu.edu/afs/cs/academic/class/15745-s15/public/lectures/L6-LLVM2-1up.pdf)

[API stuff (LLVM Programmer's Manual)](https://llvm.org/docs/ProgrammersManual.html#the-isa-cast-and-dyn-cast-templates)

[Building plugin on Windows (LLVM Discourse)](https://discourse.llvm.org/t/clang-wont-run-example-plugins-on-windows/57231/2)

[Old post on building PrintFunctionNames plugin](https://discourse.llvm.org/t/building-the-example-plugin-printfunctionnames/53604)

[Video on LLVM development on Windows (YouTube)](https://www.youtube.com/watch?v=zlD2MpU7XIw)

## C++
[Boost Safe Numerics Introduction](https://www.boost.org/doc/libs/1_76_0/libs/safe_numerics/doc/html/introduction.html)

# Microsoft
[Are there overflow-check math functions for MSVC? (StackOverflow)](https://stackoverflow.com/questions/69565333/are-there-overflow-check-math-functions-for-msvc)

[SafeInt Library documentation (Microsoft)](https://learn.microsoft.com/en-us/cpp/safeint/safeint-library?view=msvc-170)

[IntSafe API documentation (Microsoft)](https://learn.microsoft.com/en-us/windows/win32/api/intsafe/)

# Academic Papers
Holistic Control-Flow Protection on Real-Time Embedded Systems with Kage

InversOS Efficient Control-Flow Protection for AArch64 Applications with Privilege Inversion

