---
hide:
  navigation.footer
  
---

# EarthCODE

![EarthCODE](https://discourse-earthcode.eox.at/uploads/default/original/1X/19dc5eaefd1525be9147c7f0bff396482b3df848.png){: .centered-logo style="max-width: 300px;" }

[EarthCODE](https://esa-earthcode.github.io/documentation/Getting%20started%20with%20EarthCODE/) is
a strategic initiative by the European Space Agency (ESA) to support Earth System Science through
FAIR and Open Science practices. It offers researchers, particularly when executing ESA R&D projects,
access to collaborative platforms with integrated tools, cloud infrastructure, and expert support—enabling more
transparent, reusable, and impactful scientific work. Researchers are encouraged to publish workflows and data,
developed on one of the supported ESA platforms or elsewhere, to the EarthCODE catalogue. By this means,
other colleagues will be enabled to find, understand, and reproduce their research.

DeepESDL is supporting EarthCODE and both platforms have been fully integrated.

More specifically,

- the usage of DeepESDL for publishing in EarthCODE is sponsored by ESA through the Network of Resources.
- A single sign-on (SSO) mechanism makes it convenient to work with both platforms
- DeepESDL offers dedicated open-source tools to ensure an efficient and fully compliant publication process to EarthCODE.

The main tool to achieve a seamless EarthCODE integration for our users is [`deep-code`](https://github.com/deepesdl/deep-code).

## deep-code
deep-code is a lightweight Python tool for publishing datasets and scientific 
workflows from DeepESDL directly to the EarthCODE open-science-catalog.
It provides both a command-line interface (CLI) and a Python API for flexible use.

---

## Prerequisites

Before using `deep-code`, you need to configure a few **authentication files** and **environment variables**.

---

### 1. GitHub Authentication (`.gitaccess` file)

`deep-code` requires a GitHub Personal Access Token (PAT) to publish your work.  
You must create a `.gitaccess` file containing your GitHub credentials.

#### Steps

1. **Generate a GitHub PAT**
   - Go to **GitHub → Settings → Developer settings → Personal access tokens**.
   - Click **Generate new token**.
   - Select the following scope:
     - `repo` – Full control of repositories (read, fork, push, pull).
   - Generate the token and copy it (GitHub will not display it again).

2. **Create a `.gitaccess` file**  
   In your **project directory** or **home folder**, create a plain text file named `.gitaccess`:

   ```text
   github-username: your-git-user
   github-token: your-personal-access-token
    ```
Replace your-git-user and your-personal-access-token with your actual GitHub username and token.

### 2. S3 Configuration (Optional)

NOTE: If you are working inside DeepESDL, skip this section.

By default, deep-code assumes datasets are stored in:
- deepesdl-public bucket, or
- a DeepESDL-specific team S3 bucket.

If your data is stored elsewhere, configure the following environment variables:

```
export S3_USER_STORAGE_BUCKET=my-test-bucket
export AWS_DEFAULT_REGION=eu-west-2
```

In Python, load them with:

```
load_dotenv()  # take environment variables
```

### 3. Metadata Input Files

To publish with deep-code, you need two simple YAML metadata files:

1. Dataset metadata (dataset_config.yaml)

2. Workflow metadata (workflow_config.yaml)

These metadata files are used to generate valid STAC Items following the EarthCODE 
Open Science Catalog (OSC) convention, and
automatically submit a pull request to register them in the catalog.

##### Dataset Metadata (Products)

Define your dataset metadata in a YAML file:

```yaml
dataset_id: The name of the dataset object within your S3 bucket
collection_id: A unique identifier for the dataset collection
osc_themes: [wildfires] Open Science theme (choose from https://opensciencedata.esa.int/themes/catalog)
documentation_link: Link to relevant documentation, publication, or handbook
access_link: Public S3 URL to the dataset
dataset_status: Status of the dataset, e.g. 'ongoing', 'completed', or 'planned'
osc_region: Geographical coverage, e.g. 'global'
cf_parameter: The main geophysical variable, ideally matching a CF standard name or OSC variable
```

Notes:

- `osc_themes` must match an existing OSC theme.
    https://opensciencedata.esa.int/themes/catalog
- `cf_parameter` should use well-established variables (from OSC or CF conventions).

##### Workflow Metadata

Define your workflow metadata in another YAML file:

```yaml
workflow_id: A unique identifier for your workflow
properties:
    title: Human-readable title of the workflow
    description: A concise summary of what the workflow does
    keywords: Relevant scientific or technical keywords
    themes: Thematic area(s) of focus (e.g. land, ocean, atmosphere) - see the above note
    license: License type (e.g. MIT, Apache-2.0, CC-BY-4.0, proprietary)
    jupyter_kernel_info:
        name: Name of the execution environment or notebook kernel
        python_version: Python version used
        env_file: Link to the environment file (YAML) used to create the notebook environment
jupyter_notebook_url: Link to the source notebook (e.g. on GitHub)
contact:
    name: Contact person's full name
    organization: Affiliated institution or company
    links:
        rel: "about"
        type: "text/html"
        href: Link to homepage or personal/institutional profile
```

### CLI Usage

deep_code provides a command-line tool called deep-code, which has several subcommands 
providing different utility functions. Use the --help option with these subcommands to 
get more details on usage.

```
(deep-code) tejas@tejas-nb:~/bc/projects/deepesdl/deep-code$ deep-code --help
Usage: deep-code [OPTIONS] COMMAND [ARGS]...

  Deep Code CLI.

Options:
  --help  Show this message and exit.

Commands:
  generate-config
  publish          Request publishing a dataset along with experiment and...
```
The CLI retrieves the Git username and personal access token from a hidden file named 
.gitaccess. Ensure this file is located in the same directory where you execute the CLI 
command.

#### Subcommands

#### 1. deep-code generate-config

Generates starter configuration templates for publishing to EarthCODE openscience catalog.

##### Usage

```
deep-code generate-config [OPTIONS]
```

##### Options

```
--output-dir, -o : Output directory (default: current)
```

##### Examples

```
deep-code generate-config
deep-code generate-config -o ./configs
```

#### 2. deep-code publish

Publishes metadata of experiment, workflow and dataset to the EarthCODE open-science 
catalog.

##### Usage

deep-code publish DATASET_CONFIG WORKFLOW_CONFIG [--environment ENVIRONMENT]

##### Arguments

```
DATASET_CONFIG - Path to the dataset configuration YAML file
(e.g., dataset-config.yaml)

WORKFLOW_CONFIG - Path to the workflow configuration YAML file
(e.g., workflow-config.yaml)
```

##### Options

```yaml
--environment, -e - Target catalog environment: production (default) | staging | testing
```

### Python API Usage

`deep-code` can also be used directly from Python or inside a Jupyter Notebook:

```
from deep_code.tools.publish import Publisher

    publisher = Publisher(
        dataset_config_path="dataset_config.yaml",
        workflow_config_path="workflow_config.yaml"
    )
    publisher.publish_all() # publish both dataset and the workflow
```
