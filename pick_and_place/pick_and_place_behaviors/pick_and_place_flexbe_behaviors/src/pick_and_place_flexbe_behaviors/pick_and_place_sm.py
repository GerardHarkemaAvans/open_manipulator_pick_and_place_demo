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
from flexbe_states.wait_state import WaitState
from miscellaneous_flexbe_states.get_tf_transform_state import GetTFTransformState
from miscellaneous_flexbe_states.message_state import MessageState
from open_manipulator_flexbe_states.set_task_space_path_state import setTaskSpacePathState
from open_manipulator_flexbe_states.srdf_set_joint_space_path_state import srdfSetJointSpacePathState
from open_manipulator_flexbe_states.srdf_set_tool_control_state import SetToolControlState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Nov 10 2021
@author: Gerard Harkema
'''
class pick_and_placeSM(Behavior):
	'''
	Demonstration of pick and place usin AR-markers
	'''


	def __init__(self):
		super(pick_and_placeSM, self).__init__()
		self.name = 'pick_and_place'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]

		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1183 y:490, x:627 y:496
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.home_pos = 'HomePos'
		_state_machine.userdata.group = 'arm'
		_state_machine.userdata.robot_name = 'open_manipulator'
		_state_machine.userdata.photo_pos = "PhotoPos"
		_state_machine.userdata.gripper_open = 0.010
		_state_machine.userdata.gripper_close = -0.002
		_state_machine.userdata.test_part_pose = ['world', 'testpoint']
		_state_machine.userdata.drop_pos = 'DropPos'
		_state_machine.userdata.id = 3

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]

		# [/MANUAL_CREATE]


		with _state_machine:
			# x:64 y:74
			OperatableStateMachine.add('GoHomePos',
										srdfSetJointSpacePathState(path_time=5.0),
										transitions={'done': 'GripperOpenPre', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'config_name': 'home_pos', 'group': 'group', 'robot_name': 'robot_name', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:721 y:176
			OperatableStateMachine.add('GetTestPartPose',
										GetTFTransformState(),
										transitions={'done': 'GoToObject', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'frames': 'test_part_pose', 'transform': 'part_pose'})

			# x:1064 y:174
			OperatableStateMachine.add('GoDropPos',
										srdfSetJointSpacePathState(path_time=5.0),
										transitions={'done': 'GripperOpen', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'config_name': 'drop_pos', 'group': 'group', 'robot_name': 'robot_name', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1064 y:374
			OperatableStateMachine.add('GoHomeAgainPos',
										srdfSetJointSpacePathState(path_time=5.0),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'config_name': 'home_pos', 'group': 'group', 'robot_name': 'robot_name', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:464 y:74
			OperatableStateMachine.add('GoPhotoPos',
										srdfSetJointSpacePathState(path_time=2.0),
										transitions={'done': 'GetMarkerPose', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'config_name': 'photo_pos', 'group': 'group', 'robot_name': 'robot_name', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:867 y:102
			OperatableStateMachine.add('GoToObject',
										setTaskSpacePathState(end_effector_name='gripper', rotation=1.57, path_time=2.0, robot_base_link='link1', offset_z=0.01),
										transitions={'done': 'GripperClose', 'failed': 'Wait'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose_stamped': 'part_pose'})

			# x:1064 y:74
			OperatableStateMachine.add('GripperClose',
										SetToolControlState(tool='gripper'),
										transitions={'done': 'GoDropPos', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_angle': 'gripper_close'})

			# x:1064 y:274
			OperatableStateMachine.add('GripperOpen',
										SetToolControlState(tool='gripper'),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_angle': 'gripper_open'})

			# x:264 y:74
			OperatableStateMachine.add('GripperOpenPre',
										SetToolControlState(tool='gripper'),
										transitions={'done': 'GoPhotoPos', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_angle': 'gripper_open'})

			# x:870 y:4
			OperatableStateMachine.add('TestPointMessage',
										MessageState(),
										transitions={'continue': 'GoToObject'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_pose'})

			# x:1072 y:5
			OperatableStateMachine.add('Wait',
										WaitState(wait_time=3.0),
										transitions={'done': 'GripperClose'},
										autonomy={'done': Autonomy.Off})

			# x:689 y:33
			OperatableStateMachine.add('GetMarkerPose',
										GetArMarkerPoseFromId(),
										transitions={'done': 'TestPointMessage', 'not_found': 'failed', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'not_found': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'id': 'id', 'pose': 'part_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]

	# [/MANUAL_FUNC]
