"""Define implementations for getting the version string from the command line arg"""


# Using a command line build setting to name a package.
def version_from_cli_impl(ctx):
    values = {"version": ctx.build_setting_value}

    # Just pass the value from the command line through. An implementation
    # could also perform validation, such as done in
    # https://github.com/bazelbuild/bazel-skylib/blob/master/rules/common_settings.bzl
    return values
