load("@rules_cc//cc:find_cc_toolchain.bzl", "find_cc_toolchain")

# Extracting variables from the toolchain to use in the package name.
def names_from_toolchains_impl(ctx):
    values = {}

    # TODO(https://github.com/bazelbuild/bazel/issues/7260): Switch from
    # calling find_cc_toolchain to direct lookup via the name.
    # cc_toolchain = ctx.toolchains["@rules_cc//cc:toolchain_type"]
    cc_toolchain = find_cc_toolchain(ctx)

    # compiler is uninformative. Use the name of the executable
    values["compiler"] = cc_toolchain.compiler_executable.split("/")[-1]
    values["cc_cpu"] = cc_toolchain.cpu
    values["libc"] = cc_toolchain.libc

    values["compilation_mode"] = ctx.var.get("COMPILATION_MODE")

    return values
