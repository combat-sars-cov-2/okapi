## About Workbench CLI - Library

The logical folder structure is a follows:

* build - the commands for all build functions
* deploy - the commands for all deployment functions
* install - the commands for all installation functions (tools, workflows, data-managers etc)
* manage - the commands to manage the workbench (galaxy and irida) servers independently
* remove - the commands to un-install tools, workflows, data-managers and plugins from irida and galaxy
* shared - this is shared common functionality (between commands)
* utils - these are general utilities useful in context.

These folders and commands are divided logical to allow extensibility of the workbench-cli tool, even beyond irida & galaxy
