"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CommandType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CommandTypeEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CommandType.ValueType],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    COMMAND_TYPE_UNSPECIFIED: _CommandType.ValueType  # 0
    COMMAND_TYPE_SCHEDULE_ACTIVITY_TASK: _CommandType.ValueType  # 1
    COMMAND_TYPE_REQUEST_CANCEL_ACTIVITY_TASK: _CommandType.ValueType  # 2
    COMMAND_TYPE_START_TIMER: _CommandType.ValueType  # 3
    COMMAND_TYPE_COMPLETE_WORKFLOW_EXECUTION: _CommandType.ValueType  # 4
    COMMAND_TYPE_FAIL_WORKFLOW_EXECUTION: _CommandType.ValueType  # 5
    COMMAND_TYPE_CANCEL_TIMER: _CommandType.ValueType  # 6
    COMMAND_TYPE_CANCEL_WORKFLOW_EXECUTION: _CommandType.ValueType  # 7
    COMMAND_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION: _CommandType.ValueType  # 8
    COMMAND_TYPE_RECORD_MARKER: _CommandType.ValueType  # 9
    COMMAND_TYPE_CONTINUE_AS_NEW_WORKFLOW_EXECUTION: _CommandType.ValueType  # 10
    COMMAND_TYPE_START_CHILD_WORKFLOW_EXECUTION: _CommandType.ValueType  # 11
    COMMAND_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION: _CommandType.ValueType  # 12
    COMMAND_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES: _CommandType.ValueType  # 13
    COMMAND_TYPE_ACCEPT_WORKFLOW_UPDATE: _CommandType.ValueType  # 14
    """Indicates that an update has been accepted for processing workflow code"""

    COMMAND_TYPE_COMPLETE_WORKFLOW_UPDATE: _CommandType.ValueType  # 15
    """Indicates that an update has completed and carries either the success or
    failure outcome of said update.
    """

class CommandType(_CommandType, metaclass=_CommandTypeEnumTypeWrapper):
    """Whenever this list of command types is changed do change the function shouldBufferEvent in mutableStateBuilder.go to make sure to do the correct event ordering."""

    pass

COMMAND_TYPE_UNSPECIFIED: CommandType.ValueType  # 0
COMMAND_TYPE_SCHEDULE_ACTIVITY_TASK: CommandType.ValueType  # 1
COMMAND_TYPE_REQUEST_CANCEL_ACTIVITY_TASK: CommandType.ValueType  # 2
COMMAND_TYPE_START_TIMER: CommandType.ValueType  # 3
COMMAND_TYPE_COMPLETE_WORKFLOW_EXECUTION: CommandType.ValueType  # 4
COMMAND_TYPE_FAIL_WORKFLOW_EXECUTION: CommandType.ValueType  # 5
COMMAND_TYPE_CANCEL_TIMER: CommandType.ValueType  # 6
COMMAND_TYPE_CANCEL_WORKFLOW_EXECUTION: CommandType.ValueType  # 7
COMMAND_TYPE_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION: CommandType.ValueType  # 8
COMMAND_TYPE_RECORD_MARKER: CommandType.ValueType  # 9
COMMAND_TYPE_CONTINUE_AS_NEW_WORKFLOW_EXECUTION: CommandType.ValueType  # 10
COMMAND_TYPE_START_CHILD_WORKFLOW_EXECUTION: CommandType.ValueType  # 11
COMMAND_TYPE_SIGNAL_EXTERNAL_WORKFLOW_EXECUTION: CommandType.ValueType  # 12
COMMAND_TYPE_UPSERT_WORKFLOW_SEARCH_ATTRIBUTES: CommandType.ValueType  # 13
COMMAND_TYPE_ACCEPT_WORKFLOW_UPDATE: CommandType.ValueType  # 14
"""Indicates that an update has been accepted for processing workflow code"""

COMMAND_TYPE_COMPLETE_WORKFLOW_UPDATE: CommandType.ValueType  # 15
"""Indicates that an update has completed and carries either the success or
failure outcome of said update.
"""

global___CommandType = CommandType
