---
license: apache-2.0
task_categories:
- robotics
tags:
- LeRobot
- LeRobot
- test
configs:
- config_name: default
  data_files: data/*/*.parquet
---

This dataset was created using [LeRobot](https://github.com/huggingface/lerobot).

## Dataset Description



- **Homepage:** [More Information Needed]
- **Paper:** [More Information Needed]
- **License:** apache-2.0

## Dataset Structure

[meta/info.json](meta/info.json):
```json
{
    "codebase_version": "v2.1",
    "robot_type": null,
    "total_episodes": 1,
    "total_frames": 927,
    "total_tasks": 1,
    "total_videos": 3,
    "total_chunks": 1,
    "chunks_size": 1000,
    "fps": 30,
    "splits": {
        "train": "0:1"
    },
    "data_path": "data/chunk-{episode_chunk:03d}/episode_{episode_index:06d}.parquet",
    "video_path": "videos/chunk-{episode_chunk:03d}/{video_key}/episode_{episode_index:06d}.mp4",
    "features": {
        "action": {
            "dtype": "float32",
            "shape": [
                25
            ],
            "names": [
                "joint_0",
                "joint_1",
                "joint_2",
                "joint_3",
                "joint_4",
                "joint_5",
                "joint_6",
                "joint_7",
                "joint_8",
                "joint_9",
                "joint_10",
                "joint_11",
                "joint_12",
                "joint_13",
                "joint_14",
                "joint_15",
                "rot_1",
                "rot_2",
                "rot_3",
                "rot_4",
                "rot_5",
                "rot_6",
                "trans_x",
                "trans_y",
                "trans_z"
            ]
        },
        "observation.state": {
            "dtype": "float32",
            "shape": [
                25
            ],
            "names": [
                "joint_0",
                "joint_1",
                "joint_2",
                "joint_3",
                "joint_4",
                "joint_5",
                "joint_6",
                "joint_7",
                "joint_8",
                "joint_9",
                "joint_10",
                "joint_11",
                "joint_12",
                "joint_13",
                "joint_14",
                "joint_15",
                "rot_1",
                "rot_2",
                "rot_3",
                "rot_4",
                "rot_5",
                "rot_6",
                "trans_x",
                "trans_y",
                "trans_z"
            ]
        },
        "timestamp": {
            "dtype": "float32",
            "shape": [
                1
            ],
            "names": null
        },
        "task_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "observation.images.main": {
            "dtype": "video",
            "shape": [
                224,
                224,
                3
            ],
            "names": [
                "height",
                "width",
                "channel"
            ],
            "info": {
                "video.fps": 30,
                "video.codec": "mp4v",
                "video.pix_fmt": "yuv420p",
                "video.is_depth_map": false,
                "has_audio": false
            }
        },
        "observation.images.secondary_0": {
            "dtype": "video",
            "shape": [
                224,
                224,
                3
            ],
            "names": [
                "height",
                "width",
                "channel"
            ],
            "info": {
                "video.fps": 30,
                "video.codec": "mp4v",
                "video.pix_fmt": "yuv420p",
                "video.is_depth_map": false,
                "has_audio": false
            }
        },
        "observation.images.secondary_1": {
            "dtype": "video",
            "shape": [
                224,
                224,
                3
            ],
            "names": [
                "height",
                "width",
                "channel"
            ],
            "info": {
                "video.fps": 30,
                "video.codec": "mp4v",
                "video.pix_fmt": "yuv420p",
                "video.is_depth_map": false,
                "has_audio": false
            }
        },
        "frame_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "episode_index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        },
        "index": {
            "dtype": "int64",
            "shape": [
                1
            ],
            "names": null
        }
    }
}
```


## Citation

**BibTeX:**

```bibtex
[More Information Needed]
```