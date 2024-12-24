load("//pkg:version.bzl", "version_from_cli_impl")
load("//pkg:toolchain.bzl", "names_from_toolchains_impl")
load("@rules_pkg//pkg:providers.bzl", "PackageVariablesInfo")

def _pkg_vars(ctx): # Functions starting with '_' are private functions and cannot be imported into other files
    """var wrapper for both version and toolchain vars"""
    version = version_from_cli_impl(ctx)
    toolchain = names_from_toolchains_impl(ctx)

    values = {}
    values.update(version)
    values.update(toolchain)
    return PackageVariablesInfo(values = values)

pkg_vars = rule(
    implementation = _pkg_vars,
    # Going forward, the preferred way to depend on a toolchain through the
    # toolchains attribute. The current C++ toolchains, however, are still not
    # using toolchain resolution, so we have to depend on the toolchain
    # directly.
    # TODO(https://github.com/bazelbuild/bazel/issues/7260): Delete the
    # _cc_toolchain attribute.
    attrs = {
        "_cc_toolchain": attr.label(
            default = Label(
                "@rules_cc//cc:current_cc_toolchain",
            ),
        ),
    },
    toolchains = ["@rules_cc//cc:toolchain_type"],
    incompatible_use_toolchain_transition = True,
    # For version
    build_setting =config.string(flag=True),
    provides = [PackageVariablesInfo],
)