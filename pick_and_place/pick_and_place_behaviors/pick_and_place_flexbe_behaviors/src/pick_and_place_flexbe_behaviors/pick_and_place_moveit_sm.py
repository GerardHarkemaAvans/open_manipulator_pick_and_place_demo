#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ar_marker_flexbe_states.get_ar_marker_pose_form_id_state import GetArMarkerPoseFromId
from flexbe_manipulation_states.moveit_to_joints_dyn_state import MoveitToJointsDynState
from flexbe_states.wait_state import WaitState
from miscellaneous_flexbe_states.get_tf_transform_state import GetTFTransformState
from miscellaneous_flexbe_states.message_state import MessageState
from open_manipulator_moveit_flexbe_states.ik_get_joints_from_pose_state import IkGetJointsFromPose
from open_manipulator_moveit_flexbe_states.srdf_state_to_moveit import SrdfStateToMoveit as open_manipulator_moveit_flexbe_states__SrdfStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Mar 14 2020
@author: Gerard Harkema
'''
class pick_and_place_moveitSM(Behavior):
	'''
	Binpicking state machine
	'''


	def __init__(self):
		super(pick_and_place_moveitSM, self).__init__()
		self.name = 'pick_and_place_moveit'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		arm_group = 'arm'
		joint_names = ['joint1', 'joint2', 'joint3', 'joint4']
		action_topic = "move_group"
		gripper_group = 'gripper'
		# x:83 y:390, x:733 y:290
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.captured_pointcloud = []
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.pick_configuration = []
		_state_machine.userdata.offset = 0.01
		_state_machine.userdata.rotation = 1.57
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.move_group = "move_group"
		_state_machine.userdata.ee_link = "end_effector_link"
		_state_machine.userdata.world = "world"
		_state_machine.userdata.frames = ["world" , "testpoint"]
		_state_machine.userdata.marker_id = 3

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:26 y:24
			OperatableStateMachine.add('GoHomeStart',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='HomePos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'GripperOpenPre', 'planning_failed': 'failed', 'control_failed': 'WaitRetry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:547 y:474
			OperatableStateMachine.add('GoDropPosition',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='DropPos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'GripperOpen', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:47 y:474
			OperatableStateMachine.add('GoHomeEnd',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='HomePos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:797 y:474
			OperatableStateMachine.add('GoHomeTransfer',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='HomePos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'GoDropPosition', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1247 y:424
			OperatableStateMachine.add('GoObjectLiftPosition',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='PreGraspPos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'GoHomeTransfer', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:547 y:24
			OperatableStateMachine.add('GoPhotoPosition',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='PhotoPos', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'WaitEffe', 'planning_failed': 'WaitEffe', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1247 y:324
			OperatableStateMachine.add('GripperClose',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='close_pnp', move_group=gripper_group, action_topic=action_topic, robot_name="", tolerance=0.0001),
										transitions={'reached': 'GoObjectLiftPosition', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:297 y:474
			OperatableStateMachine.add('GripperOpen',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='open', move_group=gripper_group, action_topic=action_topic, robot_name="", tolerance=0.0001),
										transitions={'reached': 'GoHomeEnd', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:297 y:24
			OperatableStateMachine.add('GripperOpenPre',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='open', move_group=gripper_group, action_topic=action_topic, robot_name="", tolerance=0.0001),
										transitions={'reached': 'GoPhotoPosition', 'planning_failed': 'WaitEffe', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1259 y:26
			OperatableStateMachine.add('IkCalcilateJointsFromPose',
										IkGetJointsFromPose(joint_names=joint_names, time_out=5.0),
										transitions={'continue': 'MoveToGraspPosition', 'failed': 'failed', 'time_out': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'time_out': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'ee_link', 'pose': 'part_pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1276 y:124
			OperatableStateMachine.add('MoveToGraspPosition',
										MoveitToJointsDynState(move_group=arm_group, action_topic=action_topic),
										transitions={'reached': 'GripperClose', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1043 y:24
			OperatableStateMachine.add('PoseMessage',
										MessageState(),
										transitions={'continue': 'IkCalcilateJointsFromPose'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_pose'})

			# x:658 y:101
			OperatableStateMachine.add('WaitEffe',
										WaitState(wait_time=1),
										transitions={'done': 'GetMarkerPose'},
										autonomy={'done': Autonomy.Off})

			# x:57 y:124
			OperatableStateMachine.add('WaitRetry',
										WaitState(wait_time=3),
										transitions={'done': 'GoHomeStart'},
										autonomy={'done': Autonomy.Off})

			# x:832 y:91
			OperatableStateMachine.add('getTransformFromTestpoint',
										GetTFTransformState(),
										transitions={'done': 'PoseMessage', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'frames': 'frames', 'transform': 'part_pose'})

			# x:831 y:24
			OperatableStateMachine.add('GetMarkerPose',
										GetArMarkerPoseFromId(),
										transitions={'done': 'PoseMessage', 'not_found': 'failed', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'not_found': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'id': 'marker_id', 'pose': 'part_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
